#pragma once
#include "RepositoryInterafce.h"
#include "Evidence.h"
#include "Action.h"
#include <memory>
#include <vector>

class Service
{
private:
	RepositoryInterface& repository;
	std::vector<Evidence> physicalCopies;
	std::vector<std::unique_ptr<Action>> undoStack{};
	std::vector<std::unique_ptr<Action>> redoStack{};
public:
	Service(RepositoryInterface& repository) : repository{repository} {}
	void add_evidence(const Evidence& evidence);
	void update_evidence(const std::string& id, const std::string& measurement, double imageClarityLevel, double quantity, const std::string& photograph);
	void delete_evidence(const std::string& id);
	std::vector<Evidence> get_evidences() const;
	int get_number_of_evidences() const;
	Evidence next_evidence();
	void save_physical_copy(const std::string& id);
	int find_evidence_index_in_physical_copies_by_id(const std::string& id) const;
	const std::vector<Evidence>& get_physical_copies() const;
	int get_number_of_physical_copies() const;
	void filter_evidences_by_measurement_and_quantity(std::vector<Evidence>& filtered_list, const std::string& measurement, const double quantity) const;
	void set_file(const std::string& file);
	Evidence get_evidence_by_id(const std::string& id);
	void undo();
	void redo();
};

