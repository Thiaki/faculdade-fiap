package br.com.fiap.aula04

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.modifier.modifierLocalConsumer
import androidx.compose.ui.text.font.FontVariation.width
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import br.com.fiap.aula04.ui.theme.Aula04Theme

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            Aula04Theme {
                // A surface container using the 'background' color from the theme
                Surface(
                    modifier = Modifier.fillMaxSize(),
                    color = MaterialTheme.colorScheme.background
                ) {
                    // BoxScreen()
                    ColumnRow()
                }
            }
        }
    }
}

@Composable
fun BoxScreen() {
    Box (contentAlignment = Alignment.TopEnd) {
        Button(
            onClick = {},
            modifier = Modifier.align(Alignment.BottomEnd)
        ) {
            Text(text = "Clique Aqui")
        }
        Text(
            text = "Fiap",
            modifier = Modifier.align(Alignment.TopStart)
        )
        Button(
            onClick = {},
            modifier = Modifier
                .align(Alignment.BottomEnd)
                .offset(x = 20.dp, y = 10.dp)
        ){
            Text(text = "Outro botão")
        }
    }
}

@Composable
fun ColumnRow() {
    Column (modifier = Modifier.background(Color.Cyan)) {
        Column (
            horizontalAlignment = Alignment.CenterHorizontally,
            verticalArrangement = Arrangement.SpaceEvenly,
            modifier = Modifier
                .background(Color.Magenta)
                .fillMaxWidth()
                .height(300.dp)
        ) {
            Button(onClick = {}){
                Text(text = "Botão 01")
            }
            Button(onClick = {}){
                Text(text = "Botão 02")
            }
            Button(onClick = {}){
                Text(text = "Botão 03")
            }
            Button(onClick = {}){
                Text(text = "Botão 04")
            }
        }
        Row (verticalAlignment = Alignment.CenterVertically,
            horizontalArrangement = Arrangement.SpaceAround,
            modifier = Modifier
                .background(Color.Green)
                .fillMaxWidth()
                .height(150.dp)
        ) {
            Button(onClick = {}){
                Text(text = "Botão 01")
            }
            Button(onClick = {}){
                Text(text = "Botão 02")
            }
        }
        Row (modifier = Modifier
            .background(Color.Yellow)
            .fillMaxWidth()
            .height(150.dp)
            ) {
            Column (modifier = Modifier
                .fillMaxWidth()
                .height(100.dp)
                .padding(8.dp)
                .background(Color.Red)
                .weight(0.3f)
            ) {}
            Column (modifier = Modifier
                .fillMaxWidth()
                .height(100.dp)
                .padding(8.dp)
                .background(Color.Blue)
                .weight(0.7f)
            ) {}
        }
    }
}