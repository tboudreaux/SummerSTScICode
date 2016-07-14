from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[217.759833,58.193472],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_143102.36+581136.5/sdB_SDSSJ_143102.36+581136.5_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_143102.36+581136.5/sdB_SDSSJ_143102.36+581136.5_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
