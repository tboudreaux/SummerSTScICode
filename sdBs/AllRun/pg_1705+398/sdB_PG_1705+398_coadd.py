from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[256.681792,39.732494],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_PG_1705+398/sdB_PG_1705+398_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_PG_1705+398/sdB_PG_1705+398_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
