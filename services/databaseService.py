class databaseServiceType:  {
  "name": str,
  "age": int | float
}


def getPerson(name):
  person = dict();
  person['name'] = name
  person['age'] = 12
  return person