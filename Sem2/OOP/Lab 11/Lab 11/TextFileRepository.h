#pragma once
#include "RepositoryInterafce.h"

class TextFileRepository : public Repository
{
protected:
	std::string fileName;
public:
	virtual std::vector<Evidence> get_evidences_from_file() const;
	virtual void save_evidences_to_file(std::vector<Evidence> evidences) const;
	TextFileRepository() : Repository{} { };
	virtual void add_evidence(const Evidence& evidence) override;
	int find_evidence_by_id(const std::string& id) const override;
	void update_evidence(const std::string& id, const std::string& measurement, const double imageClarityLevel, const double quantity, const std::string& photograph) override;
	void delete_evidence(const std::string& id) override;
	std::vector<Evidence> get_evidences() const override;
	int get_number_of_evidences() const override;
	Evidence next_evidence() override;
	Evidence get_evidence_by_id(const std::string& id) const override;
	void set_file_name(const std::string& file);
	std::string get_file_name() const;
};

