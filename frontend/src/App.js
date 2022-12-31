import './App.css';
import React from 'react';


class App extends React.Component {

    state = {
        ws: null
    };

    componentDidMount() {
        const ws = new WebSocket('ws://localhost:8000/ws')
        ws.onmessage = this.onMessage
        this.state.ws = ws
    }

    componentWillUnmount() {
        const ws = this.state.ws;
        ws.close()
    }

    onMessage = (ev) => {
        const recv = JSON.parse(ev.data)
        const messages = document.getElementById('messages');
        const message = document.createElement('div');
        const content = document.createTextNode(recv.count + ': ' + recv.message);
        message.appendChild(content)
        messages.appendChild(message)

    }

    sendMessage = (ev) => {
        ev.preventDefault();
        const input = document.getElementById("messageText");
        const ws = this.state.ws;
        const data = {
            message: input.value
        }
        ws.send(JSON.stringify(data))
        input.value = ''
    }

    render() {
        return (
            <div className="container">
                <div>
                <h1>WebMessage</h1>
                <form action="" onSubmit={this.sendMessage}>
                    <input type="text" id="messageText" autoComplete="off"/>
                    <button>Send</button>
                </form>
                <h3>Messages</h3>
                <div id='messages'/>
                </div>
            </div>
        )
    }
}

export default App;