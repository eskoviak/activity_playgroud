//
//  activity.hpp
//
//  Created by Edmund L Skoviak on 11/5/23.
//

#ifndef ACTIVITY
#define ACTIVITY
#include <iostream>
#include <string>
#include <cstdlib>
#include <pqxx/pqxx>


// connect.cpp
pqxx::connection get_pq_connect();
  
// activity.cpp
std::map<int, std::string> get_exercises();

#endif /* activity.hpp*/