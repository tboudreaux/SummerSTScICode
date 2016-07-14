from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[263.328375,55.444139],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_173318.81+552638.9/sdB_sdssj_173318.81+552638.9_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_173318.81+552638.9/sdB_sdssj_173318.81+552638.9_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
