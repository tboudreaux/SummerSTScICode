from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[251.081,45.39075],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_164419.44+452326.7/sdB_sdssj_164419.44+452326.7_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_164419.44+452326.7/sdB_sdssj_164419.44+452326.7_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
