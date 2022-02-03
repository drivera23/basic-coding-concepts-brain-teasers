// create a simple struct that can have input data and prints it out.
#include <iostream>
#include <string>
using namespace std;

struct d_o_b{ //date of birth
    int month; // 1-12
    int day; // 1-31
    int year; // YYYY
};

struct Human{
    
    string first_name;
    string last_name;
    int age;
    d_o_b dob; 

    void set_name(string firstname, string lastname){
        first_name = firstname;
        last_name = lastname;
    };

    string get_name(){
        return first_name + " " + last_name;
    };

    void salute(){
        cout << "My name is " << get_name() << endl;
    };
    
    void set_age(int age_dob){
        age = age_dob;
    };
    
    void get_age(){
        cout << "My age in years is: "<< age << endl;
    };

    int get_birth_month(){
        return dob.month;
    };

    int get_birth_day(){
        return dob.day;
    };

    int get_birth_year(){
        return dob.year;
    };

    void set_birthday(int month, int day, int year){
        dob.month = month;
        dob.day = day;
        dob.year = year;
    }

    void present_birthday(){
        cout << "My birthday is " << dob.month << "/"<< dob.day << "/" << dob.year << "!" << endl; 
    }
};


int main() {

    Human Human_a; 
    string first_name, last_name;
    int month, year, day, age;
    cout << "Hello! Add characteristics to the human!" << endl;
    cout << "What is your first name? "; cin >> first_name;
    cout << "What is your last name? "; cin >> last_name;
    Human_a.set_name(first_name, last_name);
    cout << "How old are you in years?: "; cin >> age;
    while (age < 1){
        cout << "Invalid age, try again: ";cin>>year;
    };
    Human_a.set_age(age);
    cout << "Month of birth? "; cin >> month;
    while (month < 1 || month > 12){
        cout << "Invalid Month, try again: "; cin >> month;
    };
    cout << "Day of birth? "; cin >> day;
    while (day < 1 || day > 31){
        cout << "Invalid day, try again: "; cin >> day;
    };
    cout << "Year of birth? "; cin >> year;
    while (year < 1){
        cout << "Invalid Year, try again: "; cin >> year;
    };
    Human_a.set_birthday(month, day, year);
    cout << "--------------------------------------------" << endl;
    cout << "After collecting the data, we get the following: " << endl;
    Human_a.salute();
    Human_a.get_age();
    Human_a.present_birthday();
    

    return 0;
}
