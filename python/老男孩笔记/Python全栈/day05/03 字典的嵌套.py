dic = {
    "name":"汪峰",
    "age":58,
    "wife":{
        "name":"国际章",
        "salary":100000,
        "age":37
    },
    "children":[
        {"name":"老大","age":18},
        {"name":"老二","age":16},
    ]
}
print(dic["children"][1]["age"])
print(dic["wife"]["salary"])