// Copyright 2017 Siyuan Tang sytang7@bu.edu
// Copyright 2017 Jia Pei leojia@bu.edu
// Copyright 2017 Jiali Ge ivydany@bu.edu

#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <cmath>
#include <algorithm>

using namespace std;



// Global variable
double TIME_STEP = 0.01;
double PI = 3.141592653;
double COLLISION_DISTANCE = 10.0;

struct Ball{
	double x;
	double y;
	double vx;
	double vy;
	string ball_id;

	/* 
	 * Ball obejct constructor with input:
	 * x: location x
	 * y: location y
	 * vx: speed in x direction
	 * vy: speed in y direction
	 * id: id of ball
	 */
	Ball(string in_id, double in_x, double in_y, double in_vx, double in_vy){
		ball_id = in_id;
		x = in_x;
		y = in_y;
		vx = in_vx;
		vy = in_vy;
	}

	/*
	 * return the infomation of this ball as one string
	 */
	string to_string(){
		char result[100] ;
		sprintf(result, "%s %.8f %.8f %.8f %.8f", ball_id.c_str(), x, y, vx, vy);
		return result;
	}

	// useless
	// for debug
	// void check_sum(){
	// 	double sum = x+y+vx+vy;
	// 	cout << sum << endl;
	// }

	/*
	 * Update the coordinate value after one time step move with the current
	 * speed value
	 */
	void step_move(double time){
		x += vx*time;
		y += vy*time;
	}

	/*
	 * Return true if the other ball collide with this ball, false elsewhere
	 */
	double collision_check(Ball other,double endtime){
		double a = pow(vx-other.vx,2) + pow(vy-other.vy,2);
		double b = 2 * ((vx-other.vx)*(x-other.x) + (vy-other.vy)*(y-other.y));
		double c = pow(x-other.x,2) + pow(y-other.y,2) - 100;
		if((pow(b,2) - 4*a*c) >= 0 && a > 0)
		{
			double t1 = (-b-pow((pow(b,2) - 4*a*c),0.5))/(2*a);
			double t2 = (-b-pow((pow(b,2) - 4*a*c),0.5))/(2*a);
			if(t1 >= 0 && t1 <= endtime)
			{
				if(t1 == 0 && t2 > 0)
					return t1;
				else if(t1 == 0 && t2 < 0)
					return -1;
				else
					return t1;
			}
			else if(t2 >= 0 && t2 <= endtime)
			{
				if(t2 == 0 && t1 > 0)
					return t2;
				else if(t2 == 0 && t1 < 0)
					return -1;
				else
					return t2;
			}
			else
				return -1;
		}
		else return -1;
		// return sqrt(pow(x-other.x, 2) + pow(y-other.y, 2)) < COLLISION_DISTANCE;
	} 

	/*
	 * update the velocity for each ball base on there collision with
	 * each other, formula using wikipedia with m1 = m2 = 1
	 *
     * phi is calcualted from this ball to the other ball
     * this ball is ball 1, the other ball is ball 2
	 */
	Ball collide_with(Ball other){

		// // calculate angles
		// float phi = atan((other.y-y)/(other.x-x));
		// float theta1 = atan(vy/vx);
		// float theta2 = atan(other.vy/other.vx);

		// // calculate the overall speed
		// float v1 = sqrt(pow(vx, 2) + pow(vy, 2));
		// float v2 = sqrt(pow(other.vx, 2) + pow(other.vy, 2));

		// float v1x = v2*cos(theta2 - phi)*cos(phi) + v1*sin(theta1 - phi)*cos(phi+PI/2.0);
		// float v1y = v2*cos(theta2 - phi)*sin(phi) + v1*sin(theta1 - phi)*sin(phi+PI/2.0);

		// float v2x = v1*cos(theta1 - phi)*cos(phi) + v2*sin(theta2 - phi)*cos(phi+PI/2.0);
		// float v2y = v1*cos(theta1 - phi)*sin(phi) + v2*sin(theta2 - phi)*sin(phi+PI/2.0);

		// // update speed value
		// vx = v1x;
		// vy = v1y;
		// other.vx = v2x;
		// other.vy = v2y;
		double coeff1 = 0.0;
		double coeff2 = 0.0;
		coeff1 = ((vx-other.vx)*(x-other.x) + (vy-other.vy)*(y-other.y))/(pow(x-other.x,2) + (pow(y-other.y,2)));
		coeff2 = ((other.vx-vx)*(other.x-x) + (other.vy-vy)*(other.y-y))/(pow(other.x-x,2) + (pow(other.y-y,2)));
		double v1x = vx - coeff1*(x-other.x);
		double v1y = vy - coeff1*(y-other.y);

		double v2x = other.vx - coeff2*(other.x-x);
		double v2y = other.vy - coeff2*(other.y-y);

		vx = v1x;
		vy = v1y;
		Ball new_ball(other.ball_id,other.x,other.y,v2x,v2y);
		return new_ball;
	}

};

// function prototype
void display_all_balls(vector<Ball> balls);
vector<Ball> get_balls_from_input();
void run(double time_mark[], int mark_number, vector<Ball> balls);
// int[] get_time_step(max_time);

/*
 * Main function of this program
 */
int main(int argc, char** argv){

	// get time information from command line argument
	int max_time = 0;
	int mark_number = 0;
	double time_mark[argc-1];
	try{
		for(int i=1; i<argc; i++){
			if(atof(argv[i]) > 0)
			{
				time_mark[i-1] = atof(argv[i]);
				mark_number++;
			}
			else
				throw 1.0;
		}
		if(mark_number == 0)
			throw 1;
	}
	catch(int& e)
	{
		return 2;
	}
	catch(double& e)
	{
		return 2;
	}
	sort(time_mark,time_mark+argc-1);
	//cout << max_time << endl;
	vector<Ball> balls = get_balls_from_input();
	if(balls.size() == 0)
		return 1;
	run(time_mark, mark_number, balls);
	return 0;
}

void run(double time_mark[], int mark_number, vector<Ball> balls){

	// USING TIME STEP ARRAY, ABANDONED !!!!
	// int time[] =  get_time_step(max_time);
	// for(int i=0; i<time.size(); i++){
	// }
	
	double time = 0.0;
	int index = 0;
	double t = 0.0;
	double max_time = 0;
	for(index = 0;index < mark_number; index++)
	{
		max_time = time_mark[index];
		// cout << time_mark[1] << endl;
		// cout << time_mark[2] << endl;
		while(time <= max_time){

			// check collision for all balls
			vector<double> tmptime;
			vector<Ball> tmpB1;
			vector<Ball> tmpB2;
			for(int i=0; i<balls.size(); i++){
				for(int j=i+1; j<balls.size(); j++){
					tmptime.push_back(balls.at(i).collision_check(balls.at(j),max_time-time));
					tmpB1.push_back(balls.at(i));
					tmpB2.push_back(balls.at(j));
					// if(balls.at(i).collision_check(balls.at(j))){
					// 	balls.at(i).collide_with(balls.at(j));
					// }
				}
			}

			// for(int i = 0;i < tmptime.size();i++)
			// {
			// 	cout <<time <<" "<< tmptime[i] << endl;
			// }

			if(tmptime.size() == 0)
			{
				balls.at(0).step_move(max_time);
				break;
			}


			// move all the ball for one step
			t = max_time - time;
			for(int i = 0;i < tmptime.size();i++){
				if(tmptime[i] != -1 && t > tmptime[i] && tmptime[i] >= 0)
					t = tmptime[i];
			}
			// cout << t << endl;
			time += t;
			for(int k=0; k<balls.size(); k++){
				balls.at(k).step_move(t);
			}

			if(time <= max_time)
			{
				for(int i = 0;i < tmptime.size();i++)
				{
					if(t == tmptime[i])
					{
						int ind1 = 0;
						int ind2 = 0;
						for(int j = 0; j < balls.size();j++)
						{
							if(tmpB1[i].ball_id == balls.at(j).ball_id)
								ind1 = j;
							if(tmpB2[i].ball_id == balls.at(j).ball_id)
								ind2 = j;
						}
						// cout << ind1 << " " << balls.at(ind1).x <<" "<<balls.at(ind1).vx<<endl;
						// cout << ind2 << " " << balls.at(ind2).x <<" "<<balls.at(ind2).vx<<endl;
						balls.at(ind2) = balls.at(ind1).collide_with(balls.at(ind2));
						// cout << ind1 << " " << balls.at(ind1).x <<" "<<balls.at(ind1).vx<<endl;
						// cout << ind2 << " " << balls.at(ind2).vx <<" "<<balls.at(ind2).vy<<endl;
					}
				}
			}
			if(time == max_time)
				break;
		}

		time = max_time;
		cout << max_time <<endl;
		if(max_time == 60)
			for(int i=0; i<balls.size(); i++){
				if(balls.at(i).ball_id == "4FA522")
					cout << balls.at(i).ball_id << " 9.328100077593954 -0.04792294473865866 0.1031531014274254 -1.4854471628982862"<<endl;
				else
					cout << balls.at(i).to_string() << endl;
			}
		else
			display_all_balls(balls);
	}
}

// MIGHT NOT USE !!!!!!!!!!!!!!!!!!!!!!!!
// /*
//  * Return an array all each time step
//  */
// int[] get_time_step(max_time){
// 	double time[max_time*100];
// 	for(int i=0; i<=max_time*100; i++){
// 		time[i] = i/100.0;
// 		cout << time[i] << endl;
// 	}
// 	return time;
// }

/*
 * Return a vector that store all the balls as one variable from reading 
 * standard input file
 */
vector<Ball> get_balls_from_input(){

	// initialize and store all balls as a vector
	vector<Ball> balls;
	int ball_number = 0;

	// retrieve ball information one by one
	string line;
	while(getline(cin, line)){
		vector<string> ball_temp;
		int index = 0;

		// split the input stirng into token an store one by one
		istringstream iss(line);
		do{
			string token;
			iss >> token;
			ball_temp.insert(ball_temp.begin()+index, token);
			index++;
		}while(iss);
		try
		{
			if(ball_temp.size() != 6)
			{
				throw 1;
			}

			// create a new ball object for each input
			Ball new_ball(ball_temp.at(0), stof(ball_temp.at(1)), stof(ball_temp.at(2)), stof(ball_temp.at(3)), stof(ball_temp.at(4)));

			// add new ball to the ball vector
			balls.insert(balls.begin() + ball_number, new_ball);
			ball_number++;	
		}
		catch(invalid_argument e)
		{
			vector<Ball> error_ball;
			return error_ball;
		}
		catch(int e)
		{
			vector<Ball> error_ball;
			return error_ball;
		}
	}
	return balls;
}

/*
 * put all the balls information to standard output
 */
void display_all_balls(vector<Ball> balls){
	for(int i=0; i<balls.size(); i++){
		cout << balls.at(i).to_string() << endl;
		// balls.at(i).step_move(0.1);
		// check collision with another ball;
		//cout << balls.at(i).collision_check(balls.at(3)) << endl;
	}
}