from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[137.26,16.202056],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj9-10_090902.40+161207.4/sdB_sdssj9-10_090902.40+161207.4_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj9-10_090902.40+161207.4/sdB_sdssj9-10_090902.40+161207.4_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()