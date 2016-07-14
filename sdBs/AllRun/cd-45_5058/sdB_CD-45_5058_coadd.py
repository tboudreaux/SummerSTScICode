from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[140.042167,-45.531942],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_CD-45_5058/sdB_CD-45_5058_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_CD-45_5058/sdB_CD-45_5058_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
