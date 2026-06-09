/**
 * Resolve the user's locale and the currency to render in.
 *
 * Return "CAD" for Canadian locale, "USD" for everything else.
 * @returns - the resolved locale and its currency code
 */
export function getLocaleCurrency(): { locale: string; currency: string } {
  const locale =
    (typeof navigator !== "undefined" && navigator.language) || "en-US";
  const { region } = new Intl.Locale(locale).maximize();
  return { locale, currency: region === "CA" ? "CAD" : "USD" };
}

/**
 * Convert a USD amount into the user's display currency.
 *
 * Stored amounts are always USD. US users see them unchanged; CA users see
 * CAD, converted with the current exchange rate.
 * @param usd - amount in USD
 * @param caExchangeRate - Canadian dollars per 1 USD
 * @returns - amount in the user's display currency
 */
export function convertFromUSD(usd: number, caExchangeRate: number): number {
  return getLocaleCurrency().currency === "CAD" ? usd * caExchangeRate : usd;
}
