import 'package:flutter/material.dart';
import 'package:flutter/services.dart';


void main() => runApp(MyApp());

class MyApp extends StatelessWidget{
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,

      home: Home(),
    );
  }
}



class Home extends StatefulWidget {
  @override
  _HomeScreenState createState() => _HomeScreenState();


}

  var convertedText = [];
  String converted;
  bool isSwitched = false;
  String _text;
  var code = {};
  var asciiChars = [];
  bool status;
  void createAscii(){
    var x = 0;
    while (x+65 <= 90){
      asciiChars.add(String.fromCharCode(x+65));
      x+=1;
    }
    x=0;
    while(x+48 < 58){
      asciiChars.add(String.fromCharCode(x+48));
          x+=1;
    }
  }
  void morseCode() {
    code = {
      'A': ".-",
      'B': "-...",
      'C': "-.-.",
      'D': "-..",
      'E': ".",
      'F': "..-.",
      'G': "--.",
      'H': "....",
      'I': "..",
      'J': ".---",
      'K': "-.-",
      'L': ".-..",
      'M': "--",
      'N': "-.",
      'O': "---",
      'P': ".--.",
      'Q': "--.-",
      'R': ".-.",
      'S': "...",
      'T': "-",
      'U': "..-",
      'V': "...-",
      'W': ".--",
      'X': "-..-",
      'Y': "-.--",
      'Z': "--..",
      '1': ".----",
      '2': "..---",
      '3': "...--",
      '4': "....-",
      '5': ".....",
      '6': "-....",
      '7': "--...",
      '8': "---..",
      '9': "----.",
      '0': "-----"
    };
  }
    String morseToText() {
      morseCode();
      convertedText.clear();
      int len = _text.length;
      for (int i = 0; i < len; i++) {
        if (_text[i] == " ") {
          convertedText.add("/");
        }
        else if(code[_text[i].toUpperCase()] != "") {
          convertedText.add(code[_text[i].toUpperCase()]+" ");
        }
      }
      return convertedText.join();
    }
  String textToMorse(){
    _text = _text+" ";
    String output = "";
    morseCode();
    var reversedCode = code.map((k,v) => MapEntry(v, k));
    convertedText.clear();
    for(int i=0;i< _text.length;i++){
      if(_text[i] == " "){
          if(reversedCode[output] != null) {
            convertedText.add(reversedCode[output]);
            output = "";
          }
      }
      else if(_text[i] == "/") {
        convertedText.add(" ");
      }
      else{
        output +=_text[i];

      }
    }
    return convertedText.join().toLowerCase();
  }
class _HomeScreenState extends State<Home>{


  final textCon = new TextEditingController();

  @override
  Widget build(BuildContext context) {
    final key = new GlobalKey<ScaffoldState>();
    return Scaffold(
      key:key,
      appBar: AppBar(
        title: Text(
          "Morse Code",
          style: TextStyle(
            fontSize: 18.0,
            letterSpacing: 2.0,
            color: Colors.white60,
          ),
        ),
        centerTitle: true,
        backgroundColor: Colors.black45,
      ),
      body: Column(
        children: <Widget>[
          Row(
            
            children: <Widget>[
              Padding(padding: EdgeInsets.symmetric(vertical: 40.0,horizontal: 15.0),
              child: new Text(
                "Morse to Text",
                style: TextStyle(
                  fontSize: 18.0,
                  letterSpacing: 2.0,
                  color: isSwitched == false ? Colors.red[600] : Colors.grey,
                  fontWeight: FontWeight.bold,
                ),
              ),
              ),

              new Switch(
                inactiveThumbColor: Colors.red[600],
                inactiveTrackColor: Colors.red[300],
                value: isSwitched,
                onChanged: (value){
                  setState(() {
                    isSwitched=value;
                    print(isSwitched);
                  });
                },
              ),
              Padding(padding: EdgeInsets.symmetric(horizontal: 15.0,vertical: 10.0),
                  child: Text(
                  "Text to Morse",
                  style: TextStyle(
                  fontSize: 18.0,
                  letterSpacing: 2.0,
                  color: isSwitched == true ? Colors.blueAccent : Colors.grey,
                  fontWeight: FontWeight.bold,
                  ),
                  ),
              ),

            ],
          ),
          Padding(padding: EdgeInsets.symmetric(horizontal: 20.0,vertical: 40.0),
          child: TextField(
            cursorColor: isSwitched == false ? Colors.red[600] : Colors.blue[600],
            controller: textCon,
            decoration: InputDecoration(
              focusedBorder: OutlineInputBorder(
                borderSide: new BorderSide(color: isSwitched == false ? Colors.red[400] : Colors.blue[400], width: 2)
              ),
              filled: true,
              fillColor: isSwitched == false ? Colors.red[200] : Colors.blue[200],
              hintText: "What do you want to convert?"
            ),
          ),
          ),
          new RaisedButton(
            color: Colors.black45,
            padding: EdgeInsets.symmetric(horizontal: 20.0,vertical: 10.0),
              child: Text(
                "Convert",
                style: TextStyle(
                  color: Colors.white60,
                  fontWeight: FontWeight.bold,
                  fontSize: 18.0,
                ),
              ),
              onPressed: (){
              setState(() {
                _text = textCon.text;
                textCon.text = "";
                morseCode();
                createAscii();
                converted = isSwitched == false ? textToMorse() : morseToText();
              });
              }),
          Padding(padding: EdgeInsets.symmetric(vertical: 20.0,horizontal: 10.0),
         child: GestureDetector(
            child: Text(
              converted == "null" || converted == null ? "" : "$converted",
              style: TextStyle(
                  color: isSwitched == false ? Colors.redAccent : Colors.blueAccent,
                  fontSize: 18.0,
                  fontWeight: FontWeight.bold
              ),
            ),
           onLongPress: (){
              Clipboard.setData(new ClipboardData(text: converted));
              key.currentState.showSnackBar(
                new SnackBar(content: new Text("Copied to Clipboard"),));
           },
    )

          )

        ],

      )
    );
  }

}

