from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[12.170333,-1.263167],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_004840.88-011547.4/sdB_sdssj_004840.88-011547.4_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_004840.88-011547.4/sdB_sdssj_004840.88-011547.4_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
