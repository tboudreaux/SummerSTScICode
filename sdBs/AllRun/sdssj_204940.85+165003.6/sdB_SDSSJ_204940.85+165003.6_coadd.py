from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[312.420208,16.834333],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_204940.85+165003.6/sdB_SDSSJ_204940.85+165003.6_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_204940.85+165003.6/sdB_SDSSJ_204940.85+165003.6_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
