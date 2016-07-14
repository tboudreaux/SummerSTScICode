from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[355.486208,20.206303],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_2339+199/sdB_pg_2339+199_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_2339+199/sdB_pg_2339+199_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
