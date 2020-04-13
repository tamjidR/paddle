import { Vector } from './paddlepy/Vector.py';
import React, { Component } from 'react';

class Game extends Component {
	
	constructor(props){
		super(props);
		this.state = {
			WIDTH: props.width,
			HEIGHT: props.height,
			BALL: {
				pos: Vector(props.width/2, props.height/2),
				radius: 20
			}
		}
	}

	draw = () => {
		const ctx = this.refs.canvas.getContext('2d');
		ctx.fillStyle = 'red';
		ctx.beginPath();
		ctx.arc(this.state.BALL.pos[0], this.state.BALL.pos[1],
				this.state.BALL.radius, 0, 2*Math.PI);
		ctx.fill();
		ctx.stroke();
	}

	componentDidMount(){
		this.draw()
	}

	render() {
		return(
			<div>
				<canvas ref="canvas" width={this.state.WIDTH} height={this.state.HEIGHT}/>
			</div>
			);
	}
}

export default Game;