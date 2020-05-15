#include "MyExceptions.h"
#include <string>

using namespace std;

ValidationException::ValidationException(std::string _message) : message{ _message }
{
}

const char* ValidationException::what() const noexcept
{
	return message.c_str();
}

RepositoryException::RepositoryException(std::string _message) : message{ _message }
{
}

const char* RepositoryException::what() const noexcept
{
	return message.c_str();
}

