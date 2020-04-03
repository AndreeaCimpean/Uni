#include "repository.h"
#include <stdlib.h>
#include <assert.h>
#include <string.h>

Repository* createRepository()
{
	Repository* repo = (Repository*)malloc(sizeof(Repository));
	if (repo == NULL)
		return NULL;
	repo->length = 0;
	return repo;
}

void destroyRepository(Repository* repo)
{
	free(repo);
}

int findPlanet(Repository* repo, Planet p)
{
	for (int i = 0; i < repo->length; ++i)
	{
		if (strcmp(getName(&repo->elems[i]), getName(&p)) == 0)
			return 1;
		return 0;
	}
}

int addPlanet(Repository* repo, Planet p)
{
	repo->elems[repo->length++] = p;
	return 0;
}

void testRepository()
{
	Repository* repo = createRepository();
	Planet p = createPlanet("Earth", "Terrestrial", 0);
	assert(addPlanet(repo, p) == 0);
}

//_CrtDumpMemoryLeaks();
