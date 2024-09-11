from mod_lib import Lib_Mange

def main():
    library = Lib_Mange()

 
    library.add_book("1001", "Operating System Concepts", "Abraham Silberschatz", "Wiley", 10, 2020, "Operating Systems")
    library.add_book("1002", "Data Structures and Algorithm Analysis", "Clifford A. Shaffer", "Pearson", 4, 2021, "Data Structures")
    library.add_book("1003", "Machine Learning: A Probabilistic Perspective", "Kevin P. Murphy", "MIT Press", 2, 2022, "Machine Learning")


    library.rem_bk("1001")


    print(library.getbk_dets("1002"))


    print(library.srch_bk("Machine Learning"))

    print(library.srch_bk("Abraham Silberschatz", by='author'))

    

    print(list(library.list_books()))

    print(library.srch_bk("Clifford A. Shaffer", by='author'))

    library.update_dets("1001", year=2023)
    
    print(library.check_avail("1002"))
    print(library.check_avail("1003"))

if __name__ == "__main__":
    main()