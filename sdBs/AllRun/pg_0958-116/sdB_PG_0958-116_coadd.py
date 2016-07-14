from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[150.174375,-11.859456],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_PG_0958-116/sdB_PG_0958-116_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_PG_0958-116/sdB_PG_0958-116_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
