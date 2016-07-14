from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[8.943667,26.915194],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_0033+266/sdB_pg_0033+266_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_0033+266/sdB_pg_0033+266_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
