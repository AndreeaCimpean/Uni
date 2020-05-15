#pragma once
#include "Action.h"
#include "Evidence.h"
#include "RepositoryInterafce.h"

class ActionRemove : public Action
{
private:
	Evidence deletedEvidence;
	RepositoryInterface& repository;
public:
	ActionRemove(const Evidence& evidence, RepositoryInterface& repository) : deletedEvidence{ evidence }, repository{ repository }{};
	void execute_undo() override;
	void execute_redo() override;
};

