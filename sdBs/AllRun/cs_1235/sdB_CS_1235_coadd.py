from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[189.596667,-62.700556],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_CS_1235/sdB_CS_1235_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_CS_1235/sdB_CS_1235_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
