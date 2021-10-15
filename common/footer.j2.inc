{#
Copyright (C) 2019-2020 Alexandros Theodotou <alex at zrythm dot org>

This file is part of Zrythm

Zrythm is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Zrythm is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.
#}
<footer>
  <div class="container footer_container">
    <div class="row">
      <div class="col-sm-8">
        <p>
        Copyright &copy; 2019-2021 {{ _('The Zrythm contributors') }} ~
        <a href="{{ url(lang + '/legal.html') }}">{{ _('Legal') }}</a> -
        <a href="{{ url(lang + '/privacy.html') }}">{{ _('Privacy') }}</a>
        </p>
      </div>
      <div class="col-sm-4">
        <right>
         <label for="donate-bitcoin"
                class="crypto_donation_label"
                title="{{ _('Donate using Bitcoin') }}">
            <img
               class="footer_btn1"
               alt="Donate using Bitcoin"
               src="{{ url('dist/fork-awesome/btc.svg') }}">
          </label>
          <input type="checkbox" id="donate-bitcoin" class="modal">
          <div>
            <div class="card fluid centered">
              <label for="donate-bitcoin" class="modal-close" ></label>
              <h3 class="section">{{ _('Donate Bitcoin (BTC)') }}</h3>
              <p>
                <img class="qr_code"
                     src="{{ url('static/images/bitcoin_qr.png') }}">
                <br>
                BTC address: bc1qjfyu2ruyfwv3r6u4hf2nvdh900djep2dlk746j
                <br>
                <a rel="payment"
                   href="bitcoin:bc1qjfyu2ruyfwv3r6u4hf2nvdh900djep2dlk746j?message=Zrythm%20donations&time=1550598458">
                  BIP-21 URI
                </a>
              </p>
            </div>
          </div>
         <label for="donate-monero"
                class="crypto_donation_label"
                title="{{ _('Donate using Monero') }}">
            <img
               class="footer_btn2"
               alt="Donate using Bitcoin"
               src="{{ url('dist/font-awesome/monero.svg') }}">
          </label>
          <input type="checkbox" id="donate-monero" class="modal">
          <div>
            <div class="card fluid centered">
              <label for="donate-monero" class="modal-close" ></label>
              <h3 class="section">{{ _('Donate Monero (XMR)') }}</h3>
              <p>
                <img class="qr_code"
                     src="{{ url('static/images/monero_qr.png') }}">
                <br>
                XMR address: <small>87YVi6nqwDhAQwfAuB8a7UeD6wrr81PJG4yBxkkGT3Ri5ng9D1E91hdbCCQsi3ZzRuXiX3aRWesS95S8ij49YMBKG3oEfnr</small>
                <br>
              </p>
            </div>
          </div>
          <a rel="payment"
             title="{{ _('Donate using PayPal') }}"
             href="https://paypal.me/zrythm">
            <img
               class="footer_btn4"
               alt="Donate using PayPal"
               src="{{ url('dist/fork-awesome/paypal.svg') }}">
          </a>
          <a rel="payment"
             title="{{ _('Donate using LiberaPay') }}"
             href="https://liberapay.com/Zrythm">
            <img
               class="footer_btn6"
               alt="Donate using LiberaPay"
               src="{{ url('dist/fork-awesome/liberapay.svg') }}">
          </a>
          <a rel="me"
             title="{{ _('Zrythm on Mastodon') }}"
             href="https://mastodon.social/@zrythm">
            <img
               class="footer_btn6"
               alt="Zrythm on Mastodon"
               src="{{ url('dist/fork-awesome/mastodon.svg') }}">
          </a>
        </right>
      </div>
    </div>
    <div class="row">
      <div class="col-sm-12">
        <p style="text-align: center; line-height: 1;"><small>
          {{ _('Zrythm and the Zrythm logo are registered trademarks of Alexandros Theodotou in the United Kingdom.') }}
          {{ _('See our {trademarkpolicy} for details.').format (
          trademarkpolicy = '<a href="' + url(lang + '/trademarks.html') + '">' +
              _('Trademark Policy') +
              '</a>') }}
        </small></p>
      </div>
    </div>
  </div>
</footer>
