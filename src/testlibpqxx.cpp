//
//  testlibpqxx.cpp
//  testlibpq
//
//  Created by Edmund L Skoviak on 11/5/23.
//

#include "activity.hpp"
#include <cstdlib>

int main(int argc, char *argv[])
{
    // (Normally you'd check for valid command-line arguments.)
  
  try{
    std::string uri = std::getenv("PG_LOCAL");
    std::string database = "activity";
    pqxx::connection c{uri+database};
    pqxx::work txn{c};
    
    // For querying just one single value, the transaction has a shorthand method
    // query_value().
    //
    // Use txn.quote() to escape and quote a C++ string for use as an SQL string
    // in a query's text.
    
    // Test 1
    std::cout << "Test 1 -- Single value" << std::endl;

    std::string exercise_query = txn.query_value<std::string>(
      "SELECT exercise_name "
      "FROM public.exercises "
      "WHERE id = 10;");

    std::cout << "Exercise:" << exercise_query << '\n';
  
    // Test 2
    std::cout << "Test 2 -- Map of exercises" << std::endl;

    std::map<int, std::string> exercises;
    pqxx::result r = txn.exec("SELECT id, exercise_name FROM public.exercises");
      
    for(const auto &row : r) {    
      int id = row[0].get<int>().value_or(0);
      std::string exercise_name = row[1].c_str();
      const auto [it, success] = exercises.insert({id, exercise_name});
    }
    
    for (const auto& [id, name] : exercises) {
      std::cout << id << '-' << name << std::endl;
    }
  
  } catch (const std::exception &e) {
      std::cerr << e.what() << std::endl;
      return 1;
  }

  return 0;

}
