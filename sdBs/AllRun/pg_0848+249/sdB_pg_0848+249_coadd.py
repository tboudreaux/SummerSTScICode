from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[132.907667,24.697419],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_0848+249/sdB_pg_0848+249_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_0848+249/sdB_pg_0848+249_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
