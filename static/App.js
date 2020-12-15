const title= () =>{
    return React.createElement(
        "div",
        {
            class : "input-group mb-3"
        },
        React.createElement("span" , {class : 'input-group-text'} , "Site Title"),
        React.createElement("input" , {type:'text' , class:'form-control' , name:"Title"}),
    )
}
const names= () =>{
    return React.createElement(
        "div",
        {
            class : "input-group mb-3"
        },
        React.createElement("span" , {class : 'input-group-text'} , "Site Name"),
        React.createElement("input" , {type:'text' , class:'form-control' , name:"Name"}),
    )
}
const theme= () =>{
    return React.createElement(
        "div",
        {
            class : "input-group mb-3"
        },
        React.createElement("span" , {class : 'input-group-text'} , "Theme(Dark/Light)"),
        React.createElement("input" , {type:'text' , class:'form-control' , name:"Theme"}),
    )
}
const area = () =>{
    return React.createElement(
        "div",
        {
            class : "input-group mb-3"
        },
        React.createElement("span" , {class : 'input-group-text'} , "Some Text"),
        React.createElement("textarea" , {class : 'form-control' , name:'para'} ),
    )
}
const btn = () =>{
    return React.createElement(
        "input",
        {
            type:'submit',
            class : 'btn btn-primary',
            value: "Submit"
        },
    )
}
const form = () =>{
    return React.createElement(
        "form" , 
        {
            action : "/data",
            method : "post"
        },
        React.createElement(title),
        React.createElement('br'),
        React.createElement(names),
        React.createElement('br'),
        React.createElement(theme),
        React.createElement('br'),
        React.createElement(area),
        React.createElement('br'),
        React.createElement(btn)
    )
}



const App = () => {
    return React.createElement(
        "div",
        {class : 'container'},
        React.createElement("h1" , {class : "display-4"} , "Static Website Generator"),
        React.createElement("p" , {class:"lead"} , "Free single page basic template generator with Bootstrap 😉"),
        React.createElement(form)
    )
};
ReactDOM.render(React.createElement(App) , document.getElementById("root"));