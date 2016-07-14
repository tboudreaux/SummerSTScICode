from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[179.225417,-3.419442],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_1154-031/sdB_pg_1154-031_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_1154-031/sdB_pg_1154-031_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
