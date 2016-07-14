from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[249.682542,67.468989],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_PG_1638+675/sdB_PG_1638+675_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_PG_1638+675/sdB_PG_1638+675_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
