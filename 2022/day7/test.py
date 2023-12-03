#!/usr/bin/env python3

def test(status):
    match status:
        case "404": print ("404")
        case _: print ("No")

    yolo = "404"
    match status:
        case s: print ("404") if s == "404" else print("No")

print(test("404"))
