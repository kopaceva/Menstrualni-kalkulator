<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Menstrualni kalkulator</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bulma/0.7.5/css/bulma.min.css">
    <script defer src="https://use.fontawesome.com/releases/v5.3.1/js/all.js"></script>
  </head>
  <body>
    <section class="hero is-danger">
      <div class="hero-body">
        <div class="container is-fluid">   
          <h1 class="title is-1">
            Menstrualni kalkulator
          </h1>
          <headquote class="subtitle"><small>
            <i>{{citat}}</i>
          </small></headquote>
        </div>
      </div>
    </section>
    <section class="section">
      <div class="container">
        <i>Današnji datum:</i> <b>{{danes_dat}}</b>
        <p>
          {{!base}}
        </p>
      </div>
    </section>
  </body>
</html>