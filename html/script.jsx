const rootElement=document.querySelector('#root');

const root=ReactDom.createRoot(rootElement);

const App = (props)=>{
    return(
        <main className="main">
            <h1>Primo Componente</h1>
            {props.children}
        </main>

    );

};


const List=()=>{
    return(
        <ul>
            <li>Php</li>
            <li>Js</li>
            <li>Python</li>


        </ul>
    );

};
root.render(
    <>
    <App>
        <h2>Lista Completa</h2>
    <List></List>
    </App>
    </>

)