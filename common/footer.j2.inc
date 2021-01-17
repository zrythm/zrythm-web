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
        Copyright &copy; 2019-2020 {{ _('The Zrythm contributors') }} ~
        <a href="{{ url(lang + '/legal.html') }}">{{ _('Legal') }}</a> -
        <a href="{{ url(lang + '/privacy.html') }}">{{ _('Privacy') }}</a>
        </p>
      </div>
      <div class="col-sm-4">
        <right>
         <label for="donate-ethereum"
                class="crypto_donation_label"
                title="{{ _('Donate using Ethereum') }}">
            <img
               class="footer_btn2"
               alt="Donate using Ethereum"
               src="{{ url('dist/fork-awesome/ethereum.svg') }}">
          </label>
          <input type="checkbox" id="donate-ethereum" class="modal">
          <div>
            <div class="card fluid centered">
              <label for="donate-ethereum" class="modal-close" ></label>
              <h3 class="section">{{ _('Donate Ethereum (ETH)') }}</h3>
              <p>
                <img src="{{ url('static/images/ethereum_qr.svg') }}">
                <br>
                ERC20 address: 0x5f63960fdad91c3603825756cbfa645089b25f78
                <br>
                <a rel="payment"
                   href="ethereum:0x5f63960fdad91c3603825756cbfa645089b25f78">
                  ERC-67 URI
                </a>
              </p>
            </div>
          </div>
         <label for="donate-bitcoin"
                class="crypto_donation_label"
                title="{{ _('Donate using Bitcoin') }}">
            <img
               class="footer_btn2"
               alt="Donate using Bitcoin"
               src="{{ url('dist/fork-awesome/btc.svg') }}">
          </label>
          <input type="checkbox" id="donate-bitcoin" class="modal">
          <div>
            <div class="card fluid centered">
              <label for="donate-bitcoin" class="modal-close" ></label>
              <h3 class="section">{{ _('Donate Bitcoin (BTC)') }}</h3>
              <p>
                <img src="{{ url('static/images/bitcoin_qr.svg') }}">
                <br>
                BTC address: 18x1qZvtzQzUY1TrDiRWFAvavS74o2ddfU
                <br>
                <a rel="payment"
                   href="bitcoin:18x1qZvtzQzUY1TrDiRWFAvavS74o2ddfU?message=Zrythm donation">
                  BIP-21 URI
                </a>
              </p>
            </div>
          </div>
          <a rel="payment"
             title="{{ _('Donate using PayPal') }}"
             href="https://paypal.me/zrythm">
            <img
               class="footer_btn6"
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
          Zrythm and the Zrythm logo are registered trademarks of Alexandros Theodotou in the United Kingdom.
          See our
          <a href="{{ url(lang + '/trademarks.html') }}">Trademark Policy</a> for details.
        </small></p>
      </div>
    </div>
  </div>
</footer>
