#pragma once
#include <string>

class ValidationException : public std::exception
{
private:
	std::string message;
public:
	ValidationException(std::string _message);
	const char* what() const noexcept override;
};

class RepositoryException : public std::exception
{
private:
	std::string message;
public:
	RepositoryException(std::string _message);
	const char* what() const noexcept override;
};

class ServiceException : public std::exception
{
private:
	std::string message;
public:
	ServiceException(std::string _message);
	const char* what() const noexcept override;
};