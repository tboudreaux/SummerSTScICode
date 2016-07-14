from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[203.982208,12.860444],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_133555.73+125137.6/sdB_sdssj_133555.73+125137.6_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_133555.73+125137.6/sdB_sdssj_133555.73+125137.6_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
