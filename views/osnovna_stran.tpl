% import model
% rebase('bulma.tpl')

    <p>
    <br>PODATKI O PREJŠNJEM CIKLU:
    </p>
    <form action="/cikel/">
        <p>
            <br><nav class="level">
                <div class="level-item has-text-centered">
                  <div>
                    <p class="heading">Dan</p>
                    <p class="title"><input class="input is-danger" type="text" name = 'v_dan' value="{{dan_vnos}}"></p>
                  </div>
                </div>
                <div class="level-item has-text-centered">
                  <div>
                    <p class="heading">Mesec</p>
                    <p class="title"><input class="input is-danger" type="text" name = 'v_mesec' value="{{mesec_vnos}}"></p>
                  </div>
                </div>
                <div class="level-item has-text-centered">
                  <div>
                    <p class="heading">Leto</p>
                    <p class="title"><input class="input is-danger" type="text" name = 'v_leto' value="{{leto_vnos}}"></p>
                  </div>
                </div>
                <div class="level-item has-text-centered">
                  <div>
                    <p class="heading">Dolžina cikla v dneh</p>
                    <p class="title"><input class="input is-danger" type="text" name = 'v_dolzina' value="{{dolzina_vnos}}"></p>
                  </div>
                </div>
                <div class="level-item has-text-centered">
                  <div>
                    <p class="heading">Trajanje menstruacije v dneh</p>
                    <p class="title"><input class="input is-danger" type="text" name = 'v_trajanje' value="{{trajanje_vnos}}"></p>
                  </div>
                </div>
                <div class="level-item has-text-centered">
                  <div>
                    <p class="has-text-white">Pritisni</p>
                    <p class="title"><button class="button is-danger" type='submit'>IZRAČUNAJ</button></p>
                  </div>
                </div>
            </nav>
        </p>
    </form>
    <p>{{!base}}</p>
