from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[33.708292,23.331631],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_0212+230/sdB_pg_0212+230_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_0212+230/sdB_pg_0212+230_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
