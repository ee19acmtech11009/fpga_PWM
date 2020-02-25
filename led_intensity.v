module LED_PWM(clk, PWM_input, LED, input2,a);
input clk;
input [3:0] PWM_input;     // 16 intensity levels
output LED;
input input2;

output reg a;

reg [4:0] PWM;

always @(posedge clk) PWM <= PWM[3:0]+PWM_input;

assign LED = PWM[4];
assign a=input2;
endmodule
