package br.com.fiap.aula07

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.ui.Modifier
import androidx.navigation.compose.*
import br.com.fiap.aula07.screens.LoginScreen
import br.com.fiap.aula07.screens.MenuScreen
import br.com.fiap.aula07.screens.PedidosScreen
import br.com.fiap.aula07.screens.PerfilScreen
import br.com.fiap.aula07.ui.theme.Aula07Theme

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            Aula07Theme {
                // A surface container using the 'background' color from the theme
                Surface(
                    modifier = Modifier.fillMaxSize(),
                    color = MaterialTheme.colorScheme.background
                ) {
                    val navController = rememberNavController()
                    NavHost(
                        navController = navController,
                        startDestination = "login"
                    ) {
                        composable(route = "login") {
                            LoginScreen(navController)
                        }
                        composable(route = "menu") {
                            MenuScreen(navController)
                        }
                        composable(route = "pedidos") {
                            PedidosScreen(navController)
                        }
                        composable(route = "perfil") {
                            PerfilScreen(navController)
                        }
                    }
                }
            }
        }
    }
}
