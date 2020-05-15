#pragma once
class Action
{
public:
	virtual void execute_undo() = 0;
	virtual void execute_redo() = 0;

};

