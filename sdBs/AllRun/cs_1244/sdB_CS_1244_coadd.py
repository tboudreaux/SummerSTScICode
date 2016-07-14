from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[191.994167,-63.086108],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_CS_1244/sdB_CS_1244_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_CS_1244/sdB_CS_1244_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
