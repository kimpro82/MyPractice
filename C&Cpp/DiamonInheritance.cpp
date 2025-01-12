// Diamond Inheritance Problem and Resolution through Virtual Inheritance
// 2025.01.06

#include <iostream>
using namespace std;

class Food 
{
public:
    void eat_deliciously() 
    {
        cout << "Yum yum yum! Delicious!" << endl;
    }
};

// Problematic diamond inheritance
class Pizza : public Food 
{
public:
    void stretch_cheese() 
    {
        cout << "The cheese stretches so much~" << endl;
    }
};

class Pasta : public Food 
{
public:
    void slurp_noodles() 
    {
        cout << "Slurp! Sucking in the noodles!" << endl;
    }
};

class PizzaPasta : public Pizza, public Pasta 
{
};

// Solution using virtual inheritance
class VPizza : virtual public Food 
{
public:
    void stretch_cheese() 
    {
        cout << "The cheese stretches so much~" << endl;
    }
};

class VPasta : virtual public Food 
{
public:
    void slurp_noodles() 
    {
        cout << "Slurp! Sucking in the noodles!" << endl;
    }
};

class VPizzaPasta : public VPizza, public VPasta 
{
};

int main() 
{
    // Problematic diamond inheritance
    PizzaPasta weird_dish;
    weird_dish.stretch_cheese();
    weird_dish.slurp_noodles();
    // weird_dish.eat_deliciously();                        // Compilation error: ambiguous call to eat_deliciously()
    weird_dish.Pizza::eat_deliciously();                    // Resolve ambiguity by specifying the class

    cout << "\n";

    // Solution using virtual inheritance
    VPizzaPasta v_weird_dish;
    v_weird_dish.stretch_cheese();
    v_weird_dish.slurp_noodles();
    v_weird_dish.eat_deliciously();                         // No ambiguity, calls Food::eat_deliciously()

    return 0;
}
