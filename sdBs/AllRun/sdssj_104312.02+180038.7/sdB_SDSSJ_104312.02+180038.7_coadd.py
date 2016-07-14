from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[160.800083,18.01075],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_104312.02+180038.7/sdB_SDSSJ_104312.02+180038.7_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_104312.02+180038.7/sdB_SDSSJ_104312.02+180038.7_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
