#include "hello_world.h"
#define BOOST_TEST_MAIN
#include <boost/test/included/unit_test_framework.hpp>

BOOST_AUTO_TEST_CASE(test_hello)
{
    BOOST_REQUIRE_EQUAL("Hello, World!", hello_world::hello());
}
