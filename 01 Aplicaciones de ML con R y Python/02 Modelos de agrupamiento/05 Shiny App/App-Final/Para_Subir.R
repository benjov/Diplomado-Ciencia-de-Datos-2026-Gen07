# Para conectar a https://login.shinyapps.io/login?redirect=%2F

library(rsconnect)


rsconnect::setAccountInfo(name='benjov',
                          token='6667F0C5CE33274A23034B3359994A9B',
                          secret='wvEmBzHd3f29P/7YIVfWC+2DLdvYrA9X31LLrWPO')


deployApp("/Users/benjamin/Documents/Personal/Cursos_UNAM/Diplomado_Acatlan_2026 Gen 07/Diplomado-Ciencia-de-Datos-2026-Gen07/01 Aplicaciones de ML con R y Python/02 Modelos de agrupamiento/05 Shiny App/App-Final",
          appName = "Tickers-App",
          appTitle = "Tickers-App",
          account = "benjov")


