//1
import { Client } from "@webscraperio/api-client-nodejs";
const client = new Client({
	token: "0sqjBg9OcSX27BW9WSV7KXlZtObVsf5ZhsWA7pIUI17NfieadJTAQczd4jzB",
	useBackoffSleep: false
});

//getting sitemaps

let generator = client.getSitemaps();
const sitemaps = await generator.getAllRecords();

// or iterate through all sitemaps manually
generator = client.getSitemaps();
for await (const record of await generator.fetchRecords()) {
	console.log(JSON.stringify(record));
}

const response = await client.createScrapingJob({
	sitemap_id: 1029598,
	driver: "fast", // "fast" or "fulljs"
	page_load_delay: 2000,
	request_interval: 2000,
	proxy: 0, // optional. 0 - no proxy, 1 - use proxy. Or proxy id for Scale plan users
	custom_id: "toi"
})
console.log(response)

const config = await client.getSitemapScheduler(1029598);

const response1 = await client.enableSitemapScheduler(1029598, {
	cron_minute: "*/10",
	cron_hour: "*",
	cron_day: "*",
	cron_month: "*",
	cron_weekday: "*",
	request_interval: 2000,
	page_load_delay: 2000,
	cron_timezone: "Europe/Riga",
	driver: "fast", // 'fast' or 'fulljs'
	proxy: 0, // optional. 0 - no proxy, 1 - use proxy. Or proxy id for Scale plan users
});
//1
import { Client } from "@webscraperio/api-client-nodejs";
const client = new Client({
	token: "0sqjBg9OcSX27BW9WSV7KXlZtObVsf5ZhsWA7pIUI17NfieadJTAQczd4jzB",
	useBackoffSleep: false
});

//getting sitemaps

let generator = client.getSitemaps();
const sitemaps = await generator.getAllRecords();

// or iterate through all sitemaps manually
generator = client.getSitemaps();
for await (const record of await generator.fetchRecords()) {
	console.log(JSON.stringify(record));
}

const response = await client.createScrapingJob({
	sitemap_id: 1029598,
	driver: "fast", // "fast" or "fulljs"
	page_load_delay: 2000,
	request_interval: 2000,
	proxy: 0, // optional. 0 - no proxy, 1 - use proxy. Or proxy id for Scale plan users
	custom_id: "toi"
})
console.log(response)

const config = await client.getSitemapScheduler(1029598);

const response1 = await client.enableSitemapScheduler(1029598, {
	cron_minute: "*/10",
	cron_hour: "*",
	cron_day: "*",
	cron_month: "*",
	cron_weekday: "*",
	request_interval: 2000,
	page_load_delay: 2000,
	cron_timezone: "Europe/Riga",
	driver: "fast", // 'fast' or 'fulljs'
	proxy: 0, // optional. 0 - no proxy, 1 - use proxy. Or proxy id for Scale plan users
});

const scrapingJobId = 17491247;
const outputFile = hello.csv;
await client.downloadScrapingJobCSV(scrapingJobId, outputFile);
//1
import { Client } from "@webscraperio/api-client-nodejs";
const client = new Client({
	token: "0sqjBg9OcSX27BW9WSV7KXlZtObVsf5ZhsWA7pIUI17NfieadJTAQczd4jzB",
	useBackoffSleep: false
});

//getting sitemaps

let generator = client.getSitemaps();
const sitemaps = await generator.getAllRecords();

// or iterate through all sitemaps manually
generator = client.getSitemaps();
for await (const record of await generator.fetchRecords()) {
	console.log(JSON.stringify(record));
}

const response = await client.createScrapingJob({
	sitemap_id: 1029598,
	driver: "fast", // "fast" or "fulljs"
	page_load_delay: 2000,
	request_interval: 2000,
	proxy: 0, // optional. 0 - no proxy, 1 - use proxy. Or proxy id for Scale plan users
	custom_id: "toi"
})
console.log(response)

const config = await client.getSitemapScheduler(1029598);

const response1 = await client.enableSitemapScheduler(1029598, {
	cron_minute: "*/10",
	cron_hour: "*",
	cron_day: "*",
	cron_month: "*",
	cron_weekday: "*",
	request_interval: 2000,
	page_load_delay: 2000,
	cron_timezone: "Europe/Riga",
	driver: "fast", // 'fast' or 'fulljs'
	proxy: 0, // optional. 0 - no proxy, 1 - use proxy. Or proxy id for Scale plan users
});

const scrapingJobId = 17491247;
const outputFile = hello.csv;
await client.downloadScrapingJobCSV(scrapingJobId, outputFile);
//1
import { Client } from "@webscraperio/api-client-nodejs";
const client = new Client({
	token: "0sqjBg9OcSX27BW9WSV7KXlZtObVsf5ZhsWA7pIUI17NfieadJTAQczd4jzB",
	useBackoffSleep: false
});

//getting sitemaps

let generator = client.getSitemaps();
const sitemaps = await generator.getAllRecords();

// or iterate through all sitemaps manually
generator = client.getSitemaps();
for await (const record of await generator.fetchRecords()) {
	console.log(JSON.stringify(record));
}

const response = await client.createScrapingJob({
	sitemap_id: 1029598,
	driver: "fast", // "fast" or "fulljs"
	page_load_delay: 2000,
	request_interval: 2000,
	proxy: 0, // optional. 0 - no proxy, 1 - use proxy. Or proxy id for Scale plan users
	custom_id: "toi"
})
console.log(response)

const config = await client.getSitemapScheduler(1029598);

const response1 = await client.enableSitemapScheduler(1029598, {
	cron_minute: "*/10",
	cron_hour: "*",
	cron_day: "*",
	cron_month: "*",
	cron_weekday: "*",
	request_interval: 2000,
	page_load_delay: 2000,
	cron_timezone: "Europe/Riga",
	driver: "fast", // 'fast' or 'fulljs'
	proxy: 0, // optional. 0 - no proxy, 1 - use proxy. Or proxy id for Scale plan users
});

const scrapingJobId = 17491247;
const outputFile = hello.csv;
await client.downloadScrapingJobCSV(scrapingJobId, outputFile);

const scrapingJobId = 17491247;
const outputFile = hello.csv;
await client.downloadScrapingJobCSV(scrapingJobId, outputFile);