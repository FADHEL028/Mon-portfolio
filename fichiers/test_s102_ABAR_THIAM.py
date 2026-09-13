#----TESTS---UNITIAIRES----
#--------------------------------------------------

#------QUESTION-1-------
from s102 import create_answers_from_text_file
def test_create_answers_from_text_file():
    assert create_answers_from_text_file("sample_answers.txt") =={"Lisa Fischer":[7, 4, 8, 5, 7, 10, 3, 7, 8, 5],"Donna Weiss":[4, 6, 2,10, 2, 10, 4, 8, 7, 9],"Justin Sanchez":[6, 5, 9, 2, 2, 7, 6, 7, 8, 4]}, "error avec sample_answers.txt"
    assert create_answers_from_text_file("empty_file.txt") == {} ,"error avec empty file"
    print("Tous les tests pour create_answers_from_text_file ont réussi !")

#------QUESTION-2-------
from s102 import Euclidean_distance
def test_Euclidean_distance():
    assert Euclidean_distance([1, 2, 3], [4, 5, 6]) == 5.196152422706632, "error avec [1,2,3] and [4,5,6]"
    assert Euclidean_distance([0, 0], [0, 0]) == 0.0, "error avec [0,0] and [0,0]"
    assert Euclidean_distance([1], [4]) == 3.0, "error avec [1] and [4]"
    print("Tous les tests pour Euclidean_distance ont réussi !")

#------QUESTION-3-------
from s102 import Euclidean_house
def test_Euclidean_house():
    assert Euclidean_house([9, 4, 5, 3, 9, 2, 5, 1, 8, 2],[{ "house": "Serpentard", "answer": [4, 6, 5, 9, 1, 7, 3, 10, 9, 8] },{ "house": "Poufsouffle",  "answer": [3, 4, 9, 3, 6, 5, 10, 1, 9, 9]}, {"house": "Serdaigle", "answer": [2, 10, 4, 5, 2, 10, 4, 3, 7, 3]}, {"house": "Gryffondor", "answer": [9, 3, 6, 2, 10, 2, 5, 1, 8, 2]}]) == "Gryffondor"
    assert Euclidean_house([1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[{ "house": "Serpentard", "answer": [10, 10, 10, 10, 10, 10, 10, 10, 10, 10] },{ "house": "Poufsouffle",  "answer": [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]}, {"house": "Serdaigle", "answer": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]}, {"house": "Gryffondor", "answer": [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]}]) == "Serdaigle"
    print("Tous les tests pour Euclidean_house ont réussi !")

#------QUESTION-4 & 5-------
from s102 import Euclidean_repartition
def test_Euclidean_repartition():
    assert Euclidean_repartition({"Alice": [1, 2, 3], "Bob": [4, 5, 6]}, [{ "house": "House1", "answer": [1, 2, 3] }, { "house": "House2", "answer": [4, 5, 6] }]) == {"Alice": "House1", "Bob": "House2"} 
    assert Euclidean_repartition({"Charlie": [0, 0], "David": [10, 10]}, [{ "house": "HouseA", "answer": [0, 0] }, { "house": "HouseB", "answer": [10, 10] }]) == {"Charlie": "HouseA", "David": "HouseB"}
    print("Tous les tests pour Euclidean_repartition ont réussi !")

#------QUESTION-6-------
from s102 import insertion_position_NN
from json import load
def test_insertion_position_NN():
    assert insertion_position_NN([10, 10, 10, 10, 10, 10, 10, 10, 10, 10], {"house": "Serdaigle", "answer": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]}, load(open("houses_ref.json"))) == 4
    assert insertion_position_NN([5, 5, 5, 5, 5, 5, 5, 5, 5, 5], {"house": "Gryffondor", "answer": [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]}, load(open("houses_ref.json"))) == 0
    print("Tous les tests pour insertion_position_NN ont réussi !")

#------QUESTION-7-------
from s102 import insertion_NN
def test_insertion_NN():
    from json import load
    assert insertion_NN([10, 10, 10, 10, 10, 10, 10, 10, 10, 10], {"house": "Serdaigle", "answer": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]}, [{"house": "Gryffondor", "answer": [9, 3, 6, 2, 10, 2, 5, 1, 8, 2]}, {"house": "Poufsouffle", "answer": [3, 4, 9, 3, 6, 5, 10, 1, 9, 9]}, {"house": "Serpentard", "answer": [4, 6, 5, 9, 1, 7, 3, 10, 9, 8]}], 5) == [{'house': 'Gryffondor', 'answer': [9, 3, 6, 2, 10, 2, 5, 1, 8, 2]}, {'house': 'Poufsouffle', 'answer': [3, 4, 9, 3, 6, 5, 10, 1, 9, 9]}, {'house': 'Serpentard', 'answer': [4, 6, 5, 9, 1, 7, 3, 10, 9, 8]}, {'house': 'Serdaigle', 'answer': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]}] 
    print("Tous les tests pour insertion_NN ont réussi !")  

#--------QUESTION-8---------
from s102 import NN
def test_NN():
    assert NN([2, 1, 5, 6, 8, 2, 4, 3, 5, 9], [{"house": "Serpentard", "answer": [4, 6, 5, 9, 1, 7, 3, 10, 9, 8] },{ "house": "Poufsouffle",  "answer": [3, 4, 9, 3, 6, 5, 10, 1, 9, 9]}, {"house": "Serdaigle", "answer": [2, 10, 4, 5, 2, 10, 4, 3, 7, 3]}, {"house": "Gryffondor", "answer": [9, 3, 6, 2, 10, 2, 5, 1, 8, 2]}], 2) == [{'house': 'Gryffondor', 'answer': [9, 3, 6, 2, 10, 2, 5, 1, 8, 2]}, {'house': 'Poufsouffle', 'answer': [3, 4, 9, 3, 6, 5, 10, 1, 9, 9]}]
    assert NN([2, 1, 5, 6, 8, 2, 4, 3, 5, 9], [{"house": "Serpentard", "answer": [4, 6, 5, 9, 1, 7, 3, 10, 9, 8] },{ "house": "Poufsouffle",  "answer": [3, 4, 9, 3, 6, 5, 10, 1, 9, 9]}, {"house": "Serdaigle", "answer": [2, 10, 4, 5, 2, 10, 4, 3, 7, 3]}, {"house": "Gryffondor", "answer": [9, 3, 6, 2, 10, 2, 5, 1, 8, 2]}], 0) == [] 
    print("Tous les tests pour NN ont réussi !")

#------QUESTION-9-------
from s102 import NN_house
def test_NN_house():
    assert NN_house([{"house": "Serpentard", "answer": [4, 6, 5, 9, 1, 7, 3, 10, 9, 8] },{ "house": "Serdaigle",  "answer": [3, 4, 9, 3, 6, 5, 10, 1, 9, 9]}, {"house": "Serdaigle", "answer": [2, 10, 4, 5, 2, 10, 4, 3, 7, 3]}, {"house": "Serpentard", "answer": [9, 3, 6, 2, 10, 2, 5, 1, 8, 2]}]) == "Serpentard"
    assert NN_house([{"house": "Serpentard", "answer": [4, 6, 5, 9, 1, 7, 3, 10, 9, 8]}, {"house": "Gryffondor", "answer": [3, 4, 9, 3, 6, 5, 10, 1, 9, 9]},{"house": "Serdaigle", "answer": [2, 10, 4, 5, 2, 10, 4, 3, 7, 3]}, {"house": "Gryffondor", "answer": [9, 3, 6, 2, 10, 2, 5, 1, 8, 2]}]) == "Gryffondor"
    print("Tous les tests pour NN_house ont réussi!")

#------QUESTION-10-------
from s102 import NN_repartition
def test_NN_repartition():
    answer = create_answers_from_text_file("questionnaire_premiere_annee_10q.txt")
    f = open("houses_multiple_refs.json")
    reference = load(f)
    f.close()
    dico_repartition_NN = load(open("NN_repartition.json"))
    assert NN_repartition(answer, reference, 1) == dico_repartition_NN
    print("Tous les tests pour NN_repartition ont réussi!")
