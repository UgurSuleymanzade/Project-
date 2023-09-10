alfavit = ["а","б","в","г","д","е","ё","ж","з","и","й","к","л","м","н","о","п","р","с","т","у","ф","х","ц","ч","ш","щ","ъ","ы","ь","э","ю","я"]
abn = input("Введите любое слово с маленькими буквами")
bukv = ()
for n in range(len(alfavit)):
    for i in range(len(abn)):    
        if alfavit[n] is abn[i]:
            print(alfavit[n], "- это", i+1, "буква в слове")
            bukv = bukv + (alfavit[n],)
print(bukv)
