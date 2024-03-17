package br.com.fiap.appcoletadelixo

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.material3.*
import androidx.navigation.compose.*
import androidx.compose.runtime.Composable
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.ui.Modifier
import androidx.compose.ui.tooling.preview.Preview
import br.com.fiap.appcoletadelixo.screens.ResultScreen
import br.com.fiap.appcoletadelixo.screens.SearchScreen
import br.com.fiap.appcoletadelixo.ui.theme.AppcoletadelixoTheme
import br.com.fiap.appcoletadelixo.ui.theme.FontKarla

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            AppcoletadelixoTheme {
                // A surface container using the 'background' color from the theme
                Surface(
                    modifier = Modifier.fillMaxSize(),
                    color = MaterialTheme.colorScheme.background
                ) {
                    val navController = rememberNavController()
                    NavHost(
                        navController = navController,
                        startDestination = "search"
                    ) {
                        composable(route = "search") {
                            SearchScreen(navController)
                        }
                        composable(route = "result/{cep}") {
                            val cep = it.arguments?.getInt("cep")
                            ResultScreen(navController, cep!!)
                        }
                    }
                }
            }
        }
    }
}
